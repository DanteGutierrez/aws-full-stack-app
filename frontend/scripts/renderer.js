const nav = document.getElementById("NAV");

const loadNav = async () => {
    let currentPage = await page_info.currentPage();
    let menu = `<li class="nav-item">
            <a class="nav-link" ${currentPage  !== 'home' ? 'onclick="navigateToPage(\'home\')"' : ''}>Home</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" ${currentPage !== 'collection' ? 'onclick="navigateToPage(\'collection\')"' : ''}>Collection</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" ${currentPage !== 'cart' ? 'onclick="navigateToPage(\'cart\')"' : ''}>Cart</a>
        </li>`
    if (await api.getAuthorization() === '') {
        menu += `<li class="nav-item" ${currentPage!== 'login' ? 'onclick="navigateToPage(\'login\')"' : ''}>
            <a class="nav-link active">Login</a>
        </li>`
    }
    else {
        menu += `<li class="nav-item" onclick="api.logout()">
            <a class="nav-link active">Logout</a>
        </li>`
    }
    nav.innerHTML = menu;
    
    if (document.getElementById('SearchContent') != null) {

        loadBooks();
    }

    if (document.getElementById('SingleBook') != null) {
        
        loadSingleBook();
    }

    if (document.getElementById('Cart') != null) {

        loadCart();
    }
}

const navigateToPage = (page) => {
    page_info.navigateToPage(page);
}

const viewBook = (id) => {
    page_info.selectBook(id);
    page_info.navigateToPage('singlebook');
}

const setError = () => [
    document.getElementById('Error').innerHTML = '<p class="text-danger">There was an issue that occured</p>'
]

const onLogin = async () => {
    let login = {
        email: document.getElementById('Email').value,
        password: document.getElementById('Password').value
    };

    let success = await api.signIn(login);

    if (success) {
        page_info.navigateToPage('home');
    }
    else {
        setError();
    }
}

const loadBooks = async (prefoundBooks) => {

    let books = [];
    if (!prefoundBooks) books = await api.getCollection();
    else books = prefoundBooks;

    if (books.length > 0) {
        let list = '';
        books.forEach(book => {
            list +=
            `<div class="card" onclick="viewBook('${book.id.$oid}')">
                <div class="row g-0">
                    <div class="col-3">
                        <img src="${book.pic}" class="img-fluid rounded-start">
                    </div>
                    <div class="col-9">
                        <div class="card-body">
                            <div class="card-title row g-0 gap-3 align-content-bottom">
                                <span class="col-auto fw-bold">${book.title}</span>
                                <span class="text-muted col-auto">${book.author}</span>
                            </div>
                            <p class="card-text">${book.condition} - ${book.is_paperback ? 'Paperback' : 'Hard Cover'} - ${book.purchase_price}</p>
                            <p class="card-text">${book.description}</span>
                        </div>
                    </div>
                </div>
            </div>`
        });
        document.getElementById("SearchContent").innerHTML = list;
    }
    else {
        document.getElementById("SearchContent").innerHTML = '<p class="text-danger">No books loaded.</p>'
    }
}

const onSearch = async () => {
    let search = {
        title: document.getElementById('Title').value,
        author: document.getElementById('Author').value,
        genre: document.getElementById('Genre').value,
    };
    // price_minimum: document.getElementById('Min').value === '' ? null : Number(document.getElementById('Min').value),
    // price_maximum: document.getElementById('Max').value === '' ? null : Number(document.getElementById('Max').value)

    let results = await api.search(search);

    loadBooks(results);
}

const loadSingleBook = async () => {

    let book = await api.getSelectedBook();

    let button = "";

    if (await page_info.isInCart(book.id.$oid)) {
        button = `<button class="btn btn-danger" onclick="removeFromCart('${book.id.$oid}'); navigateToPage('singlebook')">Remove From Cart</button> `;
    }
    else {
        button = `<button class="btn btn-success" onclick="addToCart('${book.id.$oid}');  navigateToPage('singlebook')">Add to Cart</button> `;
    }

    document.getElementById('SingleBook').innerHTML = `
    <img class="col-4" src="${book.pic}">
    <h2>${book.title}</h2>
    <h3>${book.author}</h3>
    <p>${book.condition} - ${book.is_paperback ? 'Paperback' : 'Hard Cover'} - ${book.purchase_price}</p>
    <p>${book.description}</span>
    <span class="col-auto">
        ${button}
    </span>`
}

const loadCart = async () => {
    let cart = await api.getCartBooks();
    // let cart = await page_info.getCart();
    

    if (cart.length > 0) {
        let list = '';
        cart.forEach(book => {
            list += `<div class="row g-0 gap-2">
                <span class="col-12">${book.title}</span>
                <span class="col-12">${book.author} - ${book.purchase_price}</span>
                <button class="btn btn-danger col-auto" onclick="removeFromCart('${book.id.$oid}'); navigateToPage('cart')">Remove</button>`
        });
        document.getElementById('Cart').innerHTML = list;
    }
    else {
        document.getElementById('Pay').setAttribute('disabled', 'disabled');
        document.getElementById('Cart').innerHTML = `<p class="text-danger"> There is nothing in your cart, add books via the collection</p>`
    }
}

const addToCart = (id) => {
    page_info.addToCart(id);
}

const removeFromCart = (id) => {
    page_info.removeFromCart(id);
}

const pay = async () => {
    let payment = {
        card_num: document.getElementById('Number').value,
        card_cvc: document.getElementById('CVC').value,
        card_exp_month: document.getElementById('Month').value,
        card_exp_year: document.getElementById('Year').value,
    };
    let success = await api.pay(payment);

    if (success) {
        navigateToPage('home');
    }
    else {
        setError();
    }
}

loadNav();