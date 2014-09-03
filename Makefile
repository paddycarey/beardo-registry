help:
	@echo "deploy - Deploy registry to the configured server"
	@echo "run - Run registry locally for development purposes"

deploy:
	docker build -t "beardo/registry-deploy" .
	docker run -t -i beardo/registry-deploy python /app/scripts/validate.py
	docker run -t -i beardo/registry-deploy fab -f /app/scripts/fabfile.py with_config deploy

run:
	docker run -t -i -p 5000:5000 registry
