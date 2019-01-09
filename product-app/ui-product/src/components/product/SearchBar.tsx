import React, { ChangeEvent } from 'react'

interface Props {
    onInStockChange: (inStock: boolean) => void
    onFilterTextChange: (filterString: string) => void
    inStockOnly: boolean
    filterText: string
}

export default class SearchBar extends React.Component<Props, any> {

    constructor(public props: Props) {
        super(props)
    }

    handleInStockOnlyChange = (e: ChangeEvent<HTMLElement>) => this.props.onInStockChange((e.target as HTMLInputElement).checked)
    handleFilterTextChange = (e: ChangeEvent<HTMLElement>) => this.props.onFilterTextChange((e.target as HTMLInputElement).value)


    render() {
        return (
            <form>
                <input type="text" placeholder="Search..." value={this.props.filterText} onChange={this.handleFilterTextChange} />
                <p>
                    <input type="checkbox" checked={this.props.inStockOnly} onChange={this.handleInStockOnlyChange} />
                    {' '}Only show products in stock
            </p>
            </form>
        )
    }
}