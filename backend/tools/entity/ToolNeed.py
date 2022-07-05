import process.entity.Proses as pr
import tools.entity.ToolType as tooltype
class ToolNeed():
    def __init__(self):
        self.toolTypeCode = tooltype.ToolType()
        self.processCode = pr.Proses()
        self.idNodeOutput = pr.Proses()
