from .gallery import GalleryApi

def initialize_routes(api):
	api.add_resource(GalleryApi, '/gallery', '/gallery/<id>')

