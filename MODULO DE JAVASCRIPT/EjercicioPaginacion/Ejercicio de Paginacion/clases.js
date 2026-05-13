export class ProductAPI {

    constructor(baseURL) {
        this.baseURL = baseURL;
    }

    async searchProducts(query, limit, skip) {

        const response = await fetch(
            `${this.baseURL}/search?q=${query}&limit=${limit}&skip=${skip}`
        );

        return await response.json();
    }
}


    export class ProductUI {

    constructor() {

        this.searchResults =
            document.getElementById('search-results');

        this.quantity =
            document.getElementById('quantity');

        this.pageInfo =
            document.getElementById('pageInfo');

        this.prevBtn =
            document.getElementById('prevBtn');

        this.nextBtn =
            document.getElementById('nextBtn');
    }


    renderProducts(products) {

        this.searchResults.innerHTML = "";


        for (let product of products) {

            this.searchResults.innerHTML += `
            <div class="bg-zinc-900 border border-zinc-800 rounded-2xl overflow-hidden">

                <img 
                    src="${product.thumbnail}" 
                    class="w-full h-48 object-cover"
                />

                <div class="p-4">

                    <h3 class="font-semibold text-white">
                        ${product.title}
                    </h3>

                    <p class="text-sm text-zinc-400 mt-1">
                        ${product.description.slice(0, 60)}...
                    </p>

                    <div class="flex justify-between items-center mt-3">

                        <span class="text-green-400 font-bold">
                            $${product.price}
                        </span>

                        <span class="text-yellow-400 text-sm">
                            ★ ${product.rating}
                        </span>

                    </div>

                </div>

            </div>
            `;
        }
    }


    updateInfo(total, currentPage, totalPages) {

        this.quantity.textContent = total;

        this.pageInfo.textContent =
            `Página ${currentPage} de ${totalPages}`;

        this.nextBtn.disabled =
            currentPage >= totalPages;

        this.prevBtn.disabled =
            currentPage <= 1;
    }


    showEmptyMessage() {

        this.searchResults.innerHTML = `
            <p class="text-zinc-400 col-span-full text-center">
                No se encontraron productos
            </p>
        `;
    }
}


    export class ProductApp {

    constructor() {

        this.searchForm =
            document.getElementById('frm-search');

        this.currentPage = 1;

        this.productsPerPage = 10;

        this.totalPages = 1;

        this.currentSearch = "phone";


        this.api = new ProductAPI(
            'https://dummyjson.com/products'
        );

        this.ui = new ProductUI();


        this.init();
    }


    async loadProducts() {

        const skip =
            (this.currentPage - 1) * this.productsPerPage;


        const data =
            await this.api.searchProducts(
                this.currentSearch,
                this.productsPerPage,
                skip
            );


        this.totalPages = Math.ceil(
            data.total / this.productsPerPage
        );


        if (data.products.length === 0) {

            this.currentSearch = "phone";

            this.currentPage = 1;

            this.loadProducts();

            return;
        }


        this.ui.renderProducts(data.products);


        this.ui.updateInfo(
            data.total,
            this.currentPage,
            this.totalPages
        );
    }


    handleSearch(event) {

        event.preventDefault();


        const input =
            this.searchForm.querySelector('input');

        const searchText = input.value;


        if (searchText.trim().length === 0)
            return;


        this.currentSearch = searchText;

        this.currentPage = 1;


        this.loadProducts();


        input.value = "";
    }


    nextPage() {

        if (this.currentPage < this.totalPages) {

            this.currentPage++;

            this.loadProducts();
        }
    }


    prevPage() {

        if (this.currentPage > 1) {

            this.currentPage--;

            this.loadProducts();
        }
    }


    init() {

        this.searchForm.addEventListener(
            'submit',
            this.handleSearch.bind(this)
        );


        this.ui.nextBtn.addEventListener(
            'click',
            this.nextPage.bind(this)
        );


        this.ui.prevBtn.addEventListener(
            'click',
            this.prevPage.bind(this)
        );


        this.loadProducts();
    }
}

