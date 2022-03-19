from ..constants import MD
from ..converter import KnowledgePostConverter


class MdConverter(KnowledgePostConverter):
    _registry_keys = [MD]

    def from_file(self, filename):
        with open(filename) as f:
            self.kp_write(f.read())
