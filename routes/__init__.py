from routes.views import blueprint as view_blueprint
from routes.apis import blueprint as api_blueprint

blueprints = [(view_blueprint, ""), (api_blueprint, "/api")]
