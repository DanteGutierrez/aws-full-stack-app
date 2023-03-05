const { app, BrowserWindow, ipcMain, ipcRenderer } = require('electron')
const path = require('path');

let mainWindow;
let pageURL = './views/';
let currentPage = '';
let authorization = '';

let selectedBook = '';
let cart = [];

let books = [
  {
      id: '0',
      title: 'Harry Potter',
      pic: '',
      author: 'J. K. Rowling',
      genre: 'Fantasy',
      purchase_price: 0.69,
      rent_price: 4.20,
      condition: 'Fair Condition',
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque eu ultrices vitae auctor eu augue ut lectus arcu. Posuere lorem ipsum dolor sit. Elit ut aliquam purus sit amet. Interdum consectetur libero id faucibus nisl tincidunt. Habitasse platea dictumst quisque sagittis.',
      is_paperback: false,
      is_available: true,
    },
  {
      id: '1',
      title: 'The Hunger Games',
      pic: '',
      author: 'Suzanne Collins',
      genre: 'Fantasy',
      purchase_price: 0.69,
      rent_price: 4.20,
      condition: 'Mint Condition',
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque eu ultrices vitae auctor eu augue ut lectus arcu. Posuere lorem ipsum dolor sit. Elit ut aliquam purus sit amet. Interdum consectetur libero id faucibus nisl tincidunt. Habitasse platea dictumst quisque sagittis.',
      is_paperback: false,
      is_available: true,
    },
  {
      id: '2',
      title: 'The Hobbit',
      pic: '',
      author: 'J. R. R. Tolkien',
      genre: 'Fantasy',
      purchase_price: 0.69,
      rent_price: 4.20,
      condition: 'Poor Condition',
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Scelerisque eu ultrices vitae auctor eu augue ut lectus arcu. Posuere lorem ipsum dolor sit. Elit ut aliquam purus sit amet. Interdum consectetur libero id faucibus nisl tincidunt. Habitasse platea dictumst quisque sagittis.',
      is_paperback: true,
      is_available: true,
    },
  ];

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

// const createChildWindow = (page, title) => {
//   childWindow = new BrowserWindow(
//     {
//       width: 500,
//       height: 300,
//       title: title,
//       autoHideMenuBar: true,
//       parent: mainWindow
//     }
//   )
  
//     childWindow.loadFile(`${pageURL}${page}.html`)
// }

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

ipcMain.on('page:change', changePage);

ipcMain.handle('page:current', () => {
  return currentPage;
});

ipcMain.handle('api:login', (event, login) => {
  authorization = 'a';
  return true;
});

ipcMain.on('api:logout', () => {
  authorization = '';
  selectedBook = '';
  cart = [];
  changePage(undefined, 'home');
});

ipcMain.handle('api:authorization', () => {
  return authorization;
});

ipcMain.handle('api:get-collection', () => {
  return books
});

ipcMain.handle('api:search', () => {
  return [];
});

ipcMain.handle('api:get-selected-book', () => {
  return books[selectedBook];
})

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

ipcMain.handle('api:get-cart', () => {
  let cart = [];
  cart.forEach(id => {
    cart.push(books[id]);
  })
  return cart;
})

ipcMain.handle('page:cart-get', () => {
  return cart;
})

app.whenReady().then(() => {
  createWindow("home", 'Library')
});