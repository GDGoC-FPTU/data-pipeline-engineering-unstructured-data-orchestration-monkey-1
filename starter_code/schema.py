from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    TODO: Khai báo các trường với kiểu dữ liệu str ở dưới.
    """
    document_id: str = Field(..., description="ID duy nhất của tài liệu")
    source_type: str = Field(..., description="Nguồn dữ liệu: PDF hoặc Video")
    author: str = Field(..., description="Tác giả hoặc người tạo nội dung")
    category: str = Field(..., description="Danh mục nội dung")
    content: str = Field(..., description="Nội dung văn bản đã được làm sạch")
    timestamp: str = Field(..., description="Thời gian tạo hoặc phát hành")