const {app, BrowserWindow, ipcMain} = require('electron')

let mainWindow;
let pageURL = './views/';

const createWindow = (page, title) => {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
      title: title,
      autoHideMenuBar: true,
      webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  })
  mainWindow.loadFile(`${pageURL}${page}.html`)
}

const createChildWindow = (page, title) => {
    childWindow = new BrowserWindow({
        width: 500,
        height: 300,
        title: title,
        autoHideMenuBar: true,
        parent: mainWindow
    })

    childWindow.loadFile(`${pageURL}${page}.html`)
}

ipcMain.on('home', (event, args) => {
  mainWindow.loadFile(`${pageURL}home.html`)
})

ipcMain.on('collection', (event, args) => {
  mainWindow.loadFile(`${pageURL}collection.html`)
})

ipcMain.on('login', (event, args) => {
  mainWindow.loadFile(`${pageURL}login.html`)
})

app.whenReady().then(() => {
  createWindow("home", 'Library')
})