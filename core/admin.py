from django.contrib import admin
from .models import  *  # import all models
from django.utils.html import format_html
#_______________________________________________________
#(01)CUSTOMER-MODEL:
#______________________________________________________
class ModelCustomerAdmin(admin.ModelAdmin):
	# The fields to be shown on the Admin page
	# The line `admin.site.register(ModelCustomer)` is used to register the `ModelCustomer` model with the
	# Django admin interface. By registering a model with `admin.site.register()`, you enable the model to
	# be managed and viewed through the Django admin site. This allows administrators to interact with the
	# model data, perform CRUD operations, and customize the display of the model in the admin interface.
	list_display        = ('customer_user','customer_mobile',)
	list_filter          = ('customer_mobile',) # filter by Available Field
	list_editable        = ('customer_mobile',)
	empty_value_display = '-empty-'

# Display the Model on the Admin Page
admin.site.register(ModelCustomer, ModelCustomerAdmin)
#______________________________________________________
#(02)CATEGORY-MODEL:
#______________________________________________________
class ModelCategoryAdmin(admin.TabularInline):
	model = ModelCategory
	prepopulated_fields  = {'category_slug':('category_name',)} # Auto Filled # Autofill Slug field from name field  

# Admin View for Category Model
class ModelCategoryAdmin(admin.ModelAdmin):
	# The fields to be shown on the Admin page
	list_display        = ('picture_displayDEF','category_name','category_availability','category_image',)
	list_filter          = ('category_availability','category_name',) # filter by Available Field
	list_editable        = ('category_availability',)
	prepopulated_fields  = {'category_slug':('category_name',)} # Auto Filled # Autofill Slug field from name field  
	empty_value_display = '-empty-'
	# inlines = [SubCategoryMODELAdmin]
	list_display_links = ('category_image','category_name') 

	# View The Image On the Admin Page
	def picture_displayDEF(self,obj):
	    return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.category_image.url))
	picture_displayDEF.short_description='Picture' 


# Add The Child Table(ProductImageMODEL) Inside The Parent Table(ProductMODEL) 
class ModelCategoryAdmin(admin.TabularInline):
	model = ModelCategory
	prepopulated_fields  = {'category_slug':('category_name',)} # Auto Filled # Autofill Slug field from name field  
#
# Admin View for Category Model
class ModelCategoryAdmin(admin.ModelAdmin):
	# The fields to be shown on the Admin page
	list_display        = ('picture_displayDEF','category_name','category_availability','category_image',)
	list_filter          = ('category_availability','category_name',) # filter by Available Field
	list_editable        = ('category_availability',)
	prepopulated_fields  = {'category_slug':('category_name',)} # Auto Filled # Autofill Slug field from name field  
	empty_value_display = '-empty-'
	# inlines = [SubCategoryMODELAdmin]
	list_display_links = ('category_image','category_name') 

	# View The Image On the Admin Page
	def picture_displayDEF(self,obj):
	    return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.category_image.url))
	picture_displayDEF.short_description='Picture' 

# Display the Model on the Admin Page
admin.site.register(ModelCategory, ModelCategoryAdmin)
#______________________________________________________
#(03)PRODUCT-MODEL:
#______________________________________________________
class ModelProductAdmin(admin.TabularInline):
	model = ModelProduct
	prepopulated_fields  = {'product_slug':('product_name',)} # Auto Filled # Autofill Slug field from name field  

# Admin View for Category Model
class ModelProductAdmin(admin.ModelAdmin):
	# The fields to be shown on the Admin page
	list_display        = ('picture_displayDEF','product_name','product_category','product_price','product_stock','product_description','product_availability','product_image',)
	# The line `list_display =
	# ('picture_displayDEF','product_name','category_available','category_image',)` in the
	# `ModelProductAdmin` class is defining the fields that will be displayed in the admin interface for
	# the `ModelProduct` model.
	list_filter          = ('product_category','product_name','product_category','product_price','product_stock','product_availability',) # filter by Available Field
	list_editable        = ('product_availability','product_category','product_price','product_stock',)
	prepopulated_fields  = {'product_slug':('product_name',)} # Auto Filled # Autofill Slug field from name field  
	empty_value_display = '-empty-'
	# inlines = [SubCategoryMODELAdmin]
	list_display_links = ('product_image','product_name') 

	# View The Image On the Admin Page
	def picture_displayDEF(self,obj):
	     return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.product_image.url))
	picture_displayDEF.short_description='Picture' 

# Display the Model on the Admin Page
admin.site.register(ModelProduct, ModelProductAdmin)
#______________________________________________________
#(04)ORDER-MODEL:
#______________________________________________________
# Admin View for Category Model
class ModelOrderAdmin(admin.ModelAdmin):
	# The fields to be shown on the Admin page
	list_display        = ('order_number','order_date','order_customer','order_status','order_is_finished',)
	# The line `list_display =
	# ('picture_displayDEF','product_name','category_available','category_image',)` in the
	# `ModelProductAdmin` class is defining the fields that will be displayed in the admin interface for
	# the `ModelProduct` model.
	list_filter          = ('order_date','order_number','order_status','order_is_finished','order_customer',) # filter by Available Field
	list_editable        = ('order_customer','order_status','order_is_finished',)
	# prepopulated_fields  = {'product_slug':('product_name',)} # Auto Filled # Autofill Slug field from name field  
	empty_value_display = '-empty-'

# Display the Model on the Admin Page
admin.site.register(ModelOrder, ModelOrderAdmin)
#______________________________________________________
#(05)Cart-MODEL:
#______________________________________________________
# Admin View for Category Model
class ModelCartAdmin(admin.ModelAdmin):
	# The fields to be shown on the Admin page
	list_display        = ('picture_displayDEF','cart_product','cart_order','cart_quantity','cart_price','cart_creation_date',)
	# The line `list_display =
	# ('picture_displayDEF','product_name','category_available','category_image',)` in the
	# `ModelProductAdmin` class is defining the fields that will be displayed in the admin interface for
	# the `ModelProduct` model.
	list_filter          = ('cart_product','cart_quantity','cart_price',) # filter by Available Field
	list_editable        = ('cart_quantity','cart_price',)
	# prepopulated_fields  = {'product_slug':('product_name',)} # Auto Filled # Autofill Slug field from name field  
	empty_value_display = '-empty-'

	# View The Image On the Admin Page
	def picture_displayDEF(self,obj):
	     return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.cart_image.url))
	picture_displayDEF.short_description='Picture' 

# Display the Model on the Admin Page
admin.site.register(ModelCart, ModelCartAdmin)













