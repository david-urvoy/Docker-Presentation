import React from 'react'

export default function ProductCategoryRow(props: { category: string, inAdditionMode: boolean, handleAdd: (category: string) => void }) {
    return (<tr>
        <th colSpan={2}>
            {props.category}
            { !props.inAdditionMode && <button type="button" onClick={() => props.handleAdd(props.category)}>+</button>}
        </th>
    </tr>)
}