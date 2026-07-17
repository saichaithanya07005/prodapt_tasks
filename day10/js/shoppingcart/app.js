let cart = [
    {
        id: 1,
        product: "Laptop",
        price: 1000,
        quantity: 1
    },
    {
        id: 2,
        product: "Mobile",
        price: 500,
        quantity: 2
    },
    {
        id: 3,
        product: "Tablet",
        price: 300,
        quantity: 1
    }
];

//Calculate total price
let totalPrice = 0;
for (let item of cart) {
    totalPrice += item.price * item.quantity;
}

console.log("Cart Items:");
for (let item of cart) {
    console.log(`${item.product} - $${item.price} x ${item.quantity} = $${item.price * item.quantity}`);
}

console.log(`\nTotal Price: $${totalPrice}`);

//Add new item to cart
let newItem = {
    id: 4,
    product: "Keyboard",
    price: 100,
    quantity: 1
};

cart.push(newItem);

//Remove item from cart (Remove product with id = 2)
cart = cart.filter((item) => item.id !== 2);

//Update quantity of item with id = 1
cart = cart.map((item) => {
    if (item.id === 1) {
        item.quantity = 2;
    }
    return item;
});

console.log("\nUpdated Cart:");
console.log(cart);
