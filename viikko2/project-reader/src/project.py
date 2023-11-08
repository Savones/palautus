class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license

        self.dependencies = "\n"
        for item in dependencies:
            self.dependencies += f"- {item}\n"

        self.authors = "\n"
        for author in authors:
            self.authors += f"- {author}\n"

        self.dev_dependencies = "\n"
        for item in dev_dependencies:
            self.dev_dependencies += f"- {item}\n"

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors: {self.authors}"
            f"\nDependencies: {self.dependencies}"
            f"\nDevelopment dependencies: {self.dev_dependencies}"
        )
