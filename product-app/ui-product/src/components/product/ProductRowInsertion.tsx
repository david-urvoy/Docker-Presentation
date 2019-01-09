import React from 'react'
import Product from '../../model/product'

interface State { name: string, price: number }
interface Props { category: string, toggleAdditionMode: (category: string) => void, handleAddition: (p: Product) => void }

export default class ProductRowInsertion extends React.Component<Props, State> {

    state: State
    constructor(props: Props) {
        super(props)
        this.state = { name: '', price: 0 }
    }

    handleNameChange = (event: React.FormEvent<HTMLInputElement>) => this.setState({ name: event.currentTarget.value })
    handlePriceChange = (event: React.FormEvent<HTMLInputElement>) => this.setState({ price: parseFloat(event.currentTarget.value) })

    render() {
        return (<tr>
            <td><input type="text" placeholder="Product Name..." onChange={this.handleNameChange} /></td>
            <td><input type="text" placeholder="Product Price..." onChange={this.handlePriceChange} /></td>
            <td>
                <button onClick={() => this.props.handleAddition({ ...this.state, category: this.props.category, stocked: true })}>V</button>
                <button onClick={() => this.props.toggleAdditionMode(this.props.category)}>X</button>
            </td>
        </tr>)
    }
}