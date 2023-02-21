const {app, BrowserWindow} = require('electron')

const createWindow = (page) => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
  })

  win.loadFile(`./views/${page}.html`)
}

app.whenReady().then(() => {
  createWindow("home")
})