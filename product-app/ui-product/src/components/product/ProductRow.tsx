import React, { StyleHTMLAttributes } from 'react'
import Product from '../../model/product';

interface ProductRowProps { product: Product, delete: (p: Product) => void, updateState: () => void }

export default class ProductRow extends React.Component<ProductRowProps, Product> {

    state: Product
    constructor(props: ProductRowProps) {
        super(props)
        this.state = props.product
    }

    updateProduct = async (updatedProduct: Product) => {
        if (this.state !== updatedProduct)
            this.setState(await (await fetch(`http://172.16.3.3:8080/product/${this.props.product.id}`, {
                method: 'PUT',
                headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
                body: JSON.stringify(updatedProduct)
            })).json() as Product)
        this.props.updateState()
    }

    render() {
        const product = this.state
        return (<tr>
            <React.Fragment>
                <ProductCell content={product.name} style={product.stocked ? {} : { color: 'red' }} handleUpdate={n => this.updateProduct({ ...product, name: n })} />
                <ProductCell content={product.price.toString()} handleUpdate={p => this.updateProduct({ ...product, price: parseInt(p) })} />
                <td><input type="checkbox" checked={product.stocked} onChange={b => this.updateProduct({ ...product, stocked: b.target.checked })} /></td>
                <td><button onClick={() => this.props.delete(this.state)}>X</button></td>
            </React.Fragment>
        </tr>)
    }
}

interface ProductCellProps { content: string, style?: StyleHTMLAttributes<Element>, handleUpdate: (updatedValue: string) => void }
interface ProductCellState { inEdition: boolean, content: string }

class ProductCell extends React.Component<ProductCellProps, ProductCellState> {
    constructor(props: ProductCellProps) {
        super(props)
        this.state = { inEdition: false, content: props.content }
    }

    handleChange = (event: React.FormEvent<HTMLInputElement>) => this.setState({ content: event.currentTarget.value })

    handleUpdate = (event: React.FormEvent<HTMLInputElement>) => {
        this.setState({ inEdition: false })
        this.props.handleUpdate(event.currentTarget.value)
    }

    render() {
        return (<td>
            {this.state.inEdition ?
                <input type="text" value={this.state.content} onChange={this.handleChange} onBlur={this.handleUpdate} autoFocus />
                :
                <span style={{ ...this.props.style }} onClick={() => this.setState({ inEdition: true })}>{this.state.content}</span>
            }
        </td>)
    }
}