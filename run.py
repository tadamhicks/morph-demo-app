from app import app

# app = create_app(config_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
