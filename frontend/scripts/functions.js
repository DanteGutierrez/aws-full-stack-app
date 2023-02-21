const ipc = window.require("electron").ipcRenderer;

const navigateToPage = (page) => {
    ipc.send(page);
}