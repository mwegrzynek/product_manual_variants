#Product manual variants

Odoo module for creating product variants manually. 
Default Odoo logic creates a set of product variants as a cartesian product of all attribute values.
This is not feasible for companies with large portfolio of products, where not all attribute combinations are
valid. The Manual Variant Creation Wizard enables user to create valid attribute combinations by hand. As an added bonus, a change of attributes does not erase all the customizations made for variants created beforehand.

##Example

Let's assume we have a product template with the following attributes and their values:

- attr1 with: 
  * val1, 
  * val2, 
  * val3
- attr2 with:
  * val4,
  * val5,
  * val6
 
With default set of modules, Odoo would autocreate the following variants:
 
- (val1, val4)
- (val1, val5)
- (val1, val6)
- (val2, val4)
- (val2, val5)
- (val2, val6)

...
etc. -- total 9 combinations.
    
Let's assume, the only valid combinations are:
  
  - (val1, val4)
  - (val1, val5)
  - (val2, val4)
  - (val2, val6)
  - (val3, val4)
  
After installation of `product_manual_variants` addon a change in attribute values of a template does not generate new variants -- only running Manual Variant Creation Wizard does. 

To create the valid combinations described above we have to run the wizard 3 times, with the following values selected:

1. attr1: val1 and attr2: val4, val5
2. attr1: val2 and attr2: val4, val6
3. attr3: val3 and attr2: val4

If a variant exists before wizard execution, it is *not* updated.


  
