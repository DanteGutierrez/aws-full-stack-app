const { contextBridge, ipc, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('versions', {
  node: () => process.versions.node,
  chrome: () => process.versions.chrome,
  electron: () => process.versions.electron,
})

contextBridge.exposeInMainWorld('api', {
    getCollection: () => ipcRenderer.invoke('api:get-collection'),
    getSelectedBook: () => ipcRenderer.invoke('api:get-selected-book'),
    getCartBooks: () => ipcRenderer.invoke('api:get-cart'),
    search: (search) => ipcRenderer.invoke('api:search', search),
    signIn: (login) => ipcRenderer.invoke('api:login', login),
    logout: () => ipcRenderer.send('api:logout'),
    getAuthorization: () => ipcRenderer.invoke('api:authorization'),
  }
);

contextBridge.exposeInMainWorld('page_info', {
  currentPage: () => ipcRenderer.invoke('page:current'),
  selectBook: (id) => ipcRenderer.send('page:set-book', id),
  navigateToPage: (page) => ipcRenderer.send('page:change', page),
  addToCart: (id) => ipcRenderer.send('page:add-cart', id),
  removeFromCart: (id) => ipcRenderer.send('page:remove-cart', id),
  isInCart: (id) => ipcRenderer.invoke('page:check-cart', id),
  getCart: () => ipcRenderer.invoke('page:cart-get'),
}
);