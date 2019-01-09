import React, { Component } from 'react'
import Product from '../../model/product'
import ProductTable from './ProductTable';
import SearchBar from './SearchBar';

interface State {
    products: Product[]
    inStockOnly: boolean
    filterText: string
}

export default class FilterableProductTable extends Component<any, State> {
    state: State
    constructor(props: any) {
        super(props)
        this.state = { inStockOnly: false, filterText: '', products: [] }
        this.updateState()
    }

    updateState = () => fetch("http://localhost:8080/product")
        .then(response => response.json())
        .then(data => this.setState({ products: data as Product[] }))

    handleInStockChange = (inStockOnly: boolean) => this.setState({ inStockOnly: inStockOnly })
    handleFilterTextChange = (filterText: string) => this.setState({ filterText: filterText })

    render() {
        return (
            <React.Fragment>
                <SearchBar onFilterTextChange={this.handleFilterTextChange} onInStockChange={this.handleInStockChange} inStockOnly={this.state.inStockOnly} filterText={this.state.filterText} />
                <ProductTable inStockOnly={this.state.inStockOnly} filterText={this.state.filterText} products={this.state.products} updateState={this.updateState} />
            </React.Fragment>
        )
    }
}