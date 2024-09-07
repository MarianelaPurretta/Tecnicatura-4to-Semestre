
const cart = []; //carrito

productos.forEach((product) => {
    const content = document.createElement("div");
    content.classList.add("card-products"); // Asegúrate de que tenga la clase correcta

    content.innerHTML = `
        <img src="${product.img}">
        <h3>${product.productName}</h3>
        <p>${product.price}</p>
    `;

    const buyButton = document.createElement("button");
    buyButton.innerText = "Comprar";

    content.append(buyButton);

    shopContent.append(content);

    buyButton.addEventListener("click", () => {
        cart.push({
            id: product.id,
            productName: product.productName,
            price: product.price,
            quanty: product.quanty,
            img: product.img,
        });
        console.log(cart); // Verifica si los productos se están agregando
    });

});
