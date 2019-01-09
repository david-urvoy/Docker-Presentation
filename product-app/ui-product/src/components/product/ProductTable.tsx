import React from 'react'
import Product from '../../model/product';
import ProductCategoryRow from './ProductCategoryRow'
import ProductRow from './ProductRow'
import ProductRowInsertion from './ProductRowInsertion';

interface Products { [categoryName: string]: Product[] }

interface ProductTableProps { inStockOnly: boolean, filterText: string, products: Product[], updateState: () => void }
interface ProductTableState { additionMode: { [category: string]: boolean }, products: { [category: string]: Product[] } }

export default class ProductTable extends React.Component<ProductTableProps, ProductTableState> {

    state: ProductTableState
    constructor(props: ProductTableProps) {
        super(props)
        this.state = { additionMode: {}, products: {} }
    }

    componentWillReceiveProps(props: ProductTableProps) {
        this.setState({
            products: props.products.reduce((products: Products, product: Product) =>
                products[product.category] ? { ...products, [product.category]: [...products[product.category], product] } : { ...products, [product.category]: [product] }, {})
        })
    }

    toggleAdditionMode = (category: string) => this.setState(state => ({ additionMode: { ...state.additionMode, [category]: !state.additionMode[category] } }))

    deleteProduct = async (product: Product) => {
        await fetch(`http://localhost:8080/product/${product.id}`, {
            method: 'DELETE',
            headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }
        })
        this.props.updateState()
    }

    handleAddition = async (product: Product) => {
        await fetch(`http://localhost:8080/product`, {
            method: 'POST',
            headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
            body: JSON.stringify(product)
        })
        this.props.updateState()
        this.toggleAdditionMode(product.category)
    }

    render() {
        return (
            <table>
                <thead><tr><th>Name</th><th>Price</th></tr></thead>
                <tbody>
                    {Object.keys(this.state.products).map(k => (
                        <React.Fragment key={k}><ProductCategoryRow category={k} inAdditionMode={this.state.additionMode[k]} handleAdd={this.toggleAdditionMode} />
                            {this.state.additionMode[k] && <ProductRowInsertion handleAddition={this.handleAddition} category={k} toggleAdditionMode={this.toggleAdditionMode} />}
                            {this.state.products[k]
                                .filter(p => p.stocked || !this.props.inStockOnly)
                                .filter(p => this.props.filterText === "" || p.name.indexOf(this.props.filterText) !== -1)
                                .map(e => <ProductRow product={e} key={e.id} delete={this.deleteProduct} updateState={this.props.updateState} />)
                            }
                        </React.Fragment>
                    ))}
                </tbody>
            </table>)
    }
}