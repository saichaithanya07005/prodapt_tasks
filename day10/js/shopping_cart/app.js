//Load JSON Data

const products = require('./products.json')

//Activity 1

console.log('\nActivity1 - Dsiplay Product Names')

products.forEach(product=>{
    console.log(`${product.name} - ₹${product.price}`)
})

//Activity 2 -Calculate Ttal Price(map)

console.log('\nActivity2 - Calculate Total Price')

const totalPrice = products.map(product=>({
    name: product.name,
    total: product.price * product.quantity
}))

console.log(totalPrice)

//Activity3 - Find Available Products
console.log('\nActivity3 - Find Available products')

const availableProducts = products.filter(product=>product.inStock)

console.log(availableProducts)

//Activity4 - Find Expensive Product >5000
console.log('\nActivity4 - Expensive Products >5000')
const expensiveProduct = products.filter(product=>product.price>5000)

console.log(expensiveProduct)

//Activity5 - Search for a Product (find - 103)
console.log("\nActivity5 - Search for a Product Availability")
const searchProduct = products.some(product => product.id==103)
console.log(searchProduct)

//Activity6 - Check product Availability
console.log("\nActivity6 - Check Product Availability")
const checkAvailable = products.some(product => !product.inStock)
console.log(checkAvailable)

//Activity7 - Verify Stock Status (every)
console.log("\nActivity7 - Verify Stock Status")
const allAvailable = products.every(product => product.inStock)

console.log(allAvailable)

//Activity8 - Calculate Grand Total (reduce)

console.log("\nActivity 8 - Calculate Grand Total")
const grandTotal = products.reduce((total, product) => {
    return total + (product.price * product.quantity);
}, 0);

console.log(grandTotal)

//Activity9 - Sort Products by Price
console.log("\nActivity 9 - Sort Products by price")
const sortProduct = [...products].sort((a,b)=>a.price-b.price)

sortProduct.forEach(product=>{
    console.log(product.name)
})

//Activity 10 - Display only Product Names

console.log("\nActivity 10 - Display Only Product Names (map)")
const displayProduct = products.map(product=>product.name)
console.log(displayProduct)

//Activity 11 - Find Product(Office cChair) Position (findIndex)
const index = products.findIndex(product => product.name ==="Office Chair")
console.log(index)

//Activity 12 - Remove Out-of-Stock Producst (filter)
const availableProducst = products.filter(product=>product.inStock)

console.log(availableProducts)

//Activity 13 Add GST (map)
const productWithGST = products.map(product=>({
    ...product,
    gst: product.price * 0.18
}))

console.log(productWithGST)

//Activity 15 - Top 3 Cheapest Products

const cheapestProduct = [...products]
.sort((a, b) => a.price - b.price)
.slice(0, 3)

cheapestProduct.forEach(product => {
    console.log(`${product.name} - ₹${product.price}`)
})

//Activity 15 - Generate Bill Summary (reduce)
console.log("\nActivity 15 - Generate Bill Summary")
const billSummary = products.reduce(
    (summary, product) => {
        summary.totalProducts++
        summary.totalPrice += product.price
        summary.totalAmount += product.price * product.quantity
        return summary
    },
    {
        totalProducts: 0,
        totalPrice: 0,
        totalAmount: 0
    }
)

console.log(billSummary)