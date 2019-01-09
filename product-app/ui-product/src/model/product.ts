export default class Product {
    constructor(public name: string,
        public price: number,
        public stocked: boolean,
        public category: string,
        public id?: number) { }
}