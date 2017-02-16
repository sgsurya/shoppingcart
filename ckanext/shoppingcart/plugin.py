import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class ShoppingcartPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'shoppingcart')
        toolkit.add_public_directory(config_,'theme/public')
    
    def after_map(self, map):
        controller = 'ckanext.shoppingcart.plugin:controller'
        map.connect('/custom',controller=controller,action='custom_page')
        return map
    
class CustomController(plugins.toolkit.BaseController):
    def custom_page(self):
        return plugins.toolkit.render('custom.html')
