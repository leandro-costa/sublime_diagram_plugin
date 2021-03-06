class BaseDiagram(object):
    def __init__(self, processor, sourceFile, targetFile, text):
        self.proc = processor
        self.text = text
        self.sourceFile = sourceFile
        self.file = targetFile

    def generate(self):
        raise NotImplementedError('abstract base class is abstract')


class BaseProcessor(object):
    DIAGRAM_CLASS = None
    CHARSET = None
    CHECK_ON_STARTUP = True

    def load(self):
        raise NotImplementedError('abstract base class is abstract')

    def extract_blocks(self, view):
        raise NotImplementedError('abstract base class is abstract')

    def process(self, sourceFile, text_blocks):
        diagrams = []
        index = 0
        for block in text_blocks:
            try:
                print("Rendering diagram for block: %r" % block)
                index = index + 1
                print("TargetFile name : %r" % sourceFile+str(index))                
                diagram = self.DIAGRAM_CLASS(self, sourceFile, sourceFile+str(index), block)
                print("Call diagram.generate()")
                rendered = diagram.generate()
                diagrams.append(rendered)
            except Exception as e:
                print("Error processing diagram: %r" % e)
                print(repr(block))
        return diagrams


class BaseViewer(object):
    def load(self):
        raise NotImplementedError('abstract base class is abstract')

    def view(self, filenames):
        raise NotImplementedError('abstract base class is abstract')
