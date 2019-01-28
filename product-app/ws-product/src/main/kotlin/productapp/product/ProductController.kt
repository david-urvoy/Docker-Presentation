package productapp.product

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.*
import org.springframework.web.bind.annotation.RequestMethod.*

@RestController
@RequestMapping("/product")
@CrossOrigin(origins = ["http://localhost:3000", "http://localhost:4000", "http://localhost:5000"])
class ProductController(@Autowired private val repository: ProductRepository) {

    @GetMapping("/{id}")
    fun get(@PathVariable id: Int) = repository.findById(id).get()

    @GetMapping("")
    fun getAll(): List<Product> = repository.findAll().map {
        it.name = "RED-${it.name}"
        it
    }

    @RequestMapping(method = [POST], path = [""])
    fun create(@RequestBody product: Product) = repository.save(product)

    @RequestMapping(method = [PUT], path = ["/{id}"])
    fun update(@PathVariable id: Int, @RequestBody updateData: Product): Product {
        val product = repository.findById(id).get()
        product.name = updateData.name
        product.price = updateData.price
        product.stocked = updateData.stocked
        return repository.save(product)
    }

    @RequestMapping(method = [DELETE], path = ["/{id}"])
    fun delete(@PathVariable id: Int) = repository.deleteById(id)

}