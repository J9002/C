const { createFFmpeg, fetchFile } = FFmpeg;
const ffmpeg = createFFmpeg({ log: false });

async function run() {
    await ffmpeg.load();
    const input = document.getElementById("folder").files;
    const zip = new JSZip();
    for (const file of input) {
        if (!file.name.endsWith(".mp4")) continue;
        const name = file.name.replace(".mp4", "");
        ffmpeg.FS("writeFile", "in.mp4", await fetchFile(file));
        await ffmpeg.run(
            "-i", "in.mp4",
            "-vf", "scale=128:160",
            "-c:v", "mpeg4",
            "-c:a", "mp3",
            name + ".amv"
        );
        const data = ffmpeg.FS("readFile", name + ".amv");
        zip.file(name + ".amv", data);
    }
    const blob = await zip.generateAsync({ type: "blob" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "converted.zip";
    a.textContent = "download zip";
    const out = document.getElementById("out");
    out.innerHTML = "";
    out.appendChild(a);
}

document.getElementById("folder").addEventListener("change", run);