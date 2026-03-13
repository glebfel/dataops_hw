c = get_config()  # noqa: F821
c.JupyterHub.bind_url = "http://:8000"
c.JupyterHub.hub_bind_url = "http://:8081"
c.JupyterHub.authenticator_class = "dummy"
c.Authenticator.admin_users = {"admin"}
c.DummyAuthenticator.password = "admin"
c.Spawner.default_url = "/lab"
c.Spawner.cmd = ["jupyterhub-singleuser"]
