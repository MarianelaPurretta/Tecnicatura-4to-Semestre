const modalOverlay = document.getElementById("modal-overlay");
const modalContainer = document.getElementById("modal-container");

const cartBtn = document.getElementById("cart-btn");
const cartCounter = document.getElementById("cart-counter");

const displayCart = () => {
    modalContainer.innerHTML = "";
    modalContainer.style.display = "block";
    modalOverlay.style.display = "block";
    // Modal Header
    const modalHeder = document.createElement("div");

    const modalClose = document.createElement("div");
    modalClose.innerText = "❌";
    modalClose.className = "modal-close";
    modalHeder.append(modalClose);

    modalClose.addEventListener("click", () => {
        modalContainer.style.display = "none";
        modalOverlay.style.display = "none";
    });

    const modalTitlte = document.createElement("div");
    modalTitlte.innerText = "Carrito";
    modalTitlte.className = "modal-title";
    modalHeder.append(modalTitlte);

    modalContainer.append(modalHeder);

    // Modal Body
    if (cart.length > 0) {
        cart.forEach((productos) => {
            const modalBody = document.createElement("div");
            modalBody.className = "modal-body";
            modalBody.innerHTML = `
        <div class="product">
                <img class="product-img" src="${productos.img}"/>
                <div class="product-info">
                    <h4>${productos.productName}
                </div>
            <div class="quantity">
                <span class="quantity-btn-decrese">-</span>
                <span class="quantity-input">${productos.quanty}</sapn>
                <span class="quantity-btn-increse">+</span>
            </div>
                <div class="price">${productos.price * productos.quanty} $</div>
                <div class="delete-product">❌</div>
        </div>
        `;
            modalContainer.append(modalBody);

            // Funcion para disminuir la cantidad de productos por el boton -
            const decrese = modalBody.querySelector(".quantity-btn-decrese");
            decrese.addEventListener("click", () => {
                // Si el producto tiene productos distintos de 1 resta
                if (productos.quanty !== 1) {
                    productos.quanty--;
                    // Llamamos a la función nuevamente para actualizar su contenido
                    displayCart();
                }
                displayCartCounter();
            });
            // Funcion para aumentar la cantidad de productos por el boton +
            const increse = modalBody.querySelector(".quantity-btn-increse");
            increse.addEventListener("click", () => {
                productos.quanty++;
                // Llamamos a la función nuevamente para actualizar su contenido
                displayCart();
                displayCartCounter();
            });

            // Funcion para eleminar el producto por el boton ❌
            const deleteProducto = modalBody.querySelector(".delete-product");

            deleteProducto.addEventListener("click", () => {
                deleteCartProduct(productos.id);
            });

        });

        // modal footer

        // Funcion que recorre con reduce y recibe 2 parametros el
        // acc = que es el acumulador
        // el representa a cada uno de los productos

        const total = cart.reduce((acc, el) =>
            acc + // donde se van guardando los resultados calculados
            el.price * el.quanty, // que es lo que va a calcular
            0 // donde inicia el conteo 
        );


        const modalFooter = document.createElement("div");
        modalFooter.className = "modal-footer";
        modalFooter.innerHTML = `
    <div class="total-price"> Total $ ${total}.00</div>
    `;

        modalContainer.append(modalFooter);
    } else {
        const modalText = document.createElement("h2")
        modalText.className = "modal-body";
        modalText.innerText = "Tu carrito está vacío";
        modalContainer.append(modalText);

    }
};

cartBtn.addEventListener("click", displayCart);


const deleteCartProduct = (id) => {
    const founId = cart.findIndex((element) => element.id === id);
    console.log(founId);
    cart.splice(founId, 1);
    displayCart();
    displayCartCounter();

};

const displayCartCounter = () => {
    const cartLength = cart.reduce((acc, el) => acc + el.quanty, 0);
    if (cart.length > 0) {
        cartCounter.style.display = "block";
        cartCounter.innerText = cartLength;
    } else {
        cartCounter.style.display = "none";
    }

}