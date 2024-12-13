from abc import ABC, abstractmethod
from copy import deepcopy

class DocumentPrototype(ABC):
    @abstractmethod
    def clone_document(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Document(DocumentPrototype):
    def __init__(self, content, images, formatting, annotations):
        self.content = content
        self.images = deepcopy(images)      # Deep copy of images list
        self.formatting = formatting
        self.annotations = deepcopy(annotations)  # Deep copy of annotations list

    def clone_document(self):
        # Deep copy of Document
        return Document(
            self.content,
            self.images,
            self.formatting,
            self.annotations
        )

    def display(self):
        print("Content:", self.content)
        print("Images:", self.images)
        print("Formatting:", self.formatting)
        print("Annotations:", self.annotations)

    # Additional methods to manipulate the document
    def add_image(self, image):
        self.images.append(image)

    def add_annotation(self, annotation):
        self.annotations.append(annotation)

images = ["Image1.png"]
annotations = ["Annotation1"]

original_doc = Document(
    "Hello, World!",
    images,
    "Basic",
    annotations
)

# Cloning the document using the prototype pattern
copied_doc = original_doc.clone_document()

# Making changes to the original document
original_doc.add_image("Image2.png")
original_doc.add_annotation("Annotation2")

# Displaying the contents of both documents
print("Original Document:")
original_doc.display()
print("\nCopied Document:")
copied_doc.display()
