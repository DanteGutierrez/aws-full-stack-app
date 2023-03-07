const { app, BrowserWindow, ipcMain, ipcRenderer } = require('electron')
const path = require('path');
const axios = require('axios');

let mainWindow;
let pageURL = './views/';
const URL = 'https://gc9uwsgig5.execute-api.us-west-1.amazonaws.com/Prod';
let currentPage = '';
let authorization = '';

let selectedBook = '';
let cart = [];

const createWindow = (page, title) => {
  mainWindow = new BrowserWindow(
    {
      width: 800,
      height: 600,
      title: title,
      autoHideMenuBar: true,
      webPreferences: {
        preload: path.join(__dirname, 'preload.js'),
        nodeIntegration: true,
      },
    }
  )

  currentPage = page;

  mainWindow.loadFile(`${pageURL}${page}.html`)
}

const changePage = (event, page) => {
  if (authorization === '' && (page !== 'home' && page !== 'login')) {
    currentPage = 'home';
  
    mainWindow.loadFile(`${pageURL}home.html`)
  }
  else {
    currentPage = page;
  
    mainWindow.loadFile(`${pageURL}${page}.html`)
  }
}

const tryLogin = async (event, login) => {
  try {
    await axios({
      method: 'post',
      url: `${URL}/auth`,
      data: login
    }).then((response) => authorization = { access_token: atob(response.data.access_token.$binary.base64) });
    return true;
  }
  catch (exception) {
    console.log(exception)
    console.log('Error on login')
    return false;
  }
}

const getBooks = async () => {
  try {
    let books = [];
    await axios({
      method: 'get',
      url: `${URL}/book`,
      headers: authorization
    }).then((response) => books = response.data);
    return books;
  }
  catch (exception) {
    console.log('Error on get book');
    return [];
  }
}

const filterBooks = async (event, filters) => {
  try {
    let books = [];
    await axios({
      method: 'get',
      url: `${URL}/book`,
      params: filters,
      headers: authorization
    }).then((response) => books = response.data);
    console.log(books);
    return books;
  }
  catch (exception) {
    console.log(exception);
    console.log('Error on search');
    return [];
  }
}

const getBookById = async (event, id) => {
  if (!id) id = selectedBook;
  try {
    let book = undefined;
    await axios({
      method: 'get',
      url: `${URL}/book/${id}`,
      headers: authorization
    }).then((response => book = response.data));
    return book;
  }
  catch (exception) {
    console.log('Error on getById');
    return undefined;
  }
}

const payment = async (event, payment) => {
  payment.books = cart;
  try {
    await axios({
      method: 'post',
      url: `${URL}/payment`,
      headers: authorization,
      data: payment
    }).then((response) => console.log(response));
    return true;
  }
  catch (exception) {
    console.log(exception)
    console.log('Error on payment');
    return false;
  }
}

ipcMain.on('page:change', changePage);

ipcMain.handle('page:current', () => {
  return currentPage;
});

ipcMain.handle('api:login', tryLogin);

ipcMain.on('api:logout', () => {
  authorization = '';
  selectedBook = '';
  cart = [];
  changePage(undefined, 'home');
});

ipcMain.handle('api:authorization', () => {
  return authorization;
});

ipcMain.handle('api:get-collection', getBooks);

ipcMain.handle('api:search', filterBooks);

ipcMain.handle('api:get-selected-book', getBookById)

ipcMain.on('page:set-book', (event, id) => {
  selectedBook = id;
})

ipcMain.on('page:add-cart', (event, id) => {
  cart.push(id);
});

ipcMain.on('page:remove-cart', (event, id) => {
  let temp = [];
  for (let i = 0; i < cart.length; i++) {
    if (cart[i] != id) {
      temp.push(cart[i]);
    }
  }
  cart = temp;
});

ipcMain.handle('page:check-cart', (event, id) => {
  return cart.some(x => x == id);
})

ipcMain.handle('api:get-cart', async () => {
  let temp = [];
  for (let i = 0; i < cart.length; i++) {
    temp.push(await getBookById(undefined, cart[i]));
  }
  return temp;
})

ipcMain.handle('page:cart-get', () => {
  return cart;
})

ipcMain.handle('api:payment', payment)

app.whenReady().then(() => {
  createWindow("home", 'Library')
});