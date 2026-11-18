import json
import re
import math
from pathlib import Path
from typing import List, Dict, Any, Tuple
from backend.config import KNOWLEDGE_BASE_DIR, OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_MODEL

# Sample Knowledge Base documents curated for ĐGNL
CURATED_KNOWLEDGE_DOCS = [
    {
        "id": "doc_geo_01",
        "domain": "geography",
        "title": "Chuyển dịch cơ cấu kinh tế nông nghiệp Đồng bằng sông Cửu Long",
        "content": "Đồng bằng sông Cửu Long là vựa lúa lớn nhất Việt Nam. Trước diễn biến biến đổi khí hậu và xâm nhập mặn nghiêm trọng trong mùa khô, mô hình luân canh một vụ lúa - một vụ tôm (lúa tôm kết hợp) tại các tỉnh Bến Tre, Trà Vinh, Cà Mau, Kiên Giang được xem là giải pháp thích ứng thông minh thuận thiên. Mùa mưa nước ngọt trồng giống lúa chịu mặn chất lượng cao, mùa khô nước lợ thả nuôi tôm sinh thái, giảm thiểu tối đa phân bón và thuốc bảo vệ thực vật."
    },
    {
        "id": "doc_geo_02",
        "domain": "geography",
        "title": "Đặc điểm phân hóa địa hình và khoáng sản thềm lục địa Việt Nam",
        "content": "Địa hình Việt Nam đồi núi chiếm 3/4 diện tích, chủ yếu là đồi núi thấp dưới 1000m. Vùng thềm lục địa phía Nam có các bể trầm tích Cửu Long, Nam Côn Sơn chứa trữ lượng dầu mỏ và khí đốt tự nhiên lớn. Hệ thống đảo và quần đảo Hoàng Sa, Trường Sa có vị trí chiến lược an ninh quốc phòng và tiềm năng phát triển kinh tế biển đa ngành."
    },
    {
        "id": "doc_hist_01",
        "domain": "history",
        "title": "Ý nghĩa lịch sử của Cách mạng tháng Tám năm 1945 và Tuyên ngôn Độc lập",
        "content": "Cách mạng tháng Tám năm 1945 thắng lợi đã phá tan xiềng xích nô lệ thực dân Pháp hơn 80 năm và phát xít Nhật, lật nhào ngai vàng phong kiến hàng nghìn năm. Ngày 2/9/1945, tại Quảng trường Ba Đình, Chủ tịch Hồ Chí Minh đọc bản Tuyên ngôn Độc lập khai sinh nước Việt Nam Dân chủ Cộng hòa, mở ra kỷ nguyên mới: kỷ nguyên độc lập tự do và nhân dân làm chủ vận mệnh đất nước."
    },
    {
        "id": "doc_hist_02",
        "domain": "history",
        "title": "Chiến dịch Điện Biên Phủ 1954 và bước ngoặt kết thúc chiến tranh",
        "content": "Chiến dịch Điện Biên Phủ diễn ra từ tháng 3 đến tháng 5 năm 1954 dưới sự chỉ huy của Đại tướng Võ Nguyên Giáp. Sau 56 ngày đêm 'khoét núi, ngủ hầm, mưa dầm, cơm vắt', quân ta đã tiêu diệt hoàn toàn tập đoàn cứ điểm mạnh nhất Đông Dương của thực dân Pháp. Thắng lợi này đập tan kế hoạch Nava và buộc chính phủ Pháp phải ký Hiệp định Genève chấm dứt chiến tranh xâm lược tại Đông Dương."
    },
    {
        "id": "doc_bio_01",
        "domain": "biology",
        "title": "Cấu trúc hệ gen, đột biến phân tử và cơ chế di truyền quần thể",
        "content": "Quần thể ngẫu phối là đơn vị sinh sản và tiến hóa cơ bản của loài trong tự nhiên. Trạng thái cân bằng di truyền Hardy-Weinberg được duy trì khi thỏa mãn các điều kiện: quần thể kích thước lớn, giao phối ngẫu nhiên, không có đột biến mới, không có chọn lọc tự nhiên và không có sự di nhập gen. Tần số tương đối của các alen p(A) và q(a) duy trì ổn định qua các thế hệ theo công thức p^2 AA + 2pq Aa + q^2 aa = 1."
    },
    {
        "id": "doc_bio_02",
        "domain": "biology",
        "title": "Công nghệ sinh học phân tử và liệu pháp gen tái tổ hợp",
        "content": "Công nghệ tái tổ hợp ADN sử dụng enzyme cắt giới hạn (restriction endonuclease) và enzyme nối ligase để đưa gen đích từ sinh vật cho vào thể truyền plasmid rồi chuyển vào vi khuẩn E.coli nhân dòng. Ứng dụng phổ biến nhất là sản xuất hormone insulin người chữa bệnh tiểu đường và chế phẩm interferon chống virus."
    },
    {
        "id": "doc_chem_01",
        "domain": "chemistry",
        "title": "Phản ứng ester hóa và cơ chế xúc tác cân bằng hóa học",
        "content": "Phản ứng ester hóa giữa acid carboxylic và alcohol là phản ứng thuận nghịch. H2SO4 đặc đóng vai trò kép: làm xúc tác acid tăng tốc độ phản ứng và hút nước làm giảm nồng độ H2O, thúc đẩy cân bằng chuyển dịch theo chiều thuận tạo nhiều ester hơn theo nguyên lý Le Chatelier. Các ester có mùi thơm hoa quả đặc trưng được ứng dụng rộng rãi làm dung môi, hương liệu thực phẩm và mỹ phẩm."
    },
    {
        "id": "doc_chem_02",
        "domain": "chemistry",
        "title": "Ăn mòn kim loại trong môi trường biển và biện pháp bảo vệ điện hóa",
        "content": "Ăn mòn điện hóa học là quá trình phá hủy kim loại do tác dụng của dung dịch chất điện ly tạo nên dòng điện micro. Để bảo vệ vỏ tàu thủy bằng thép (Fe), người ta gắn các khối kẽm (Zn) vào phần thân ngập nước. Do kẽm có tính khử mạnh hơn sắt, kẽm đóng vai trò là cực âm (anot) bị ăn mòn trước, bảo vệ lớp sắt nguyên vẹn."
    },
    {
        "id": "doc_phys_01",
        "domain": "physics",
        "title": "Sóng dừng, giao thoa sóng cơ học và hiện tượng cộng hưởng",
        "content": "Sóng dừng hình thành do sự chồng chập giữa sóng tới và sóng phản xạ ngược chiều trên cùng một phương truyền. Khi hai đầu dây cố định, chiều dài dây thỏa mãn L = k * (lambda / 2), với k là số bó sóng (số bụng sóng), khoảng cách giữa hai nút liên tiếp hoặc hai bụng liên tiếp luôn bằng nửa bước sóng (lambda / 2)."
    },
    {
        "id": "doc_lit_01",
        "domain": "vietnamese",
        "title": "Chủ nghĩa nhân đạo và số phận con người trong văn xuôi hiện thực 1930 - 1945",
        "content": "Văn học hiện thực phê phán giai đoạn 1930 - 1945 với các tác giả tiêu biểu như Nam Cao, Kim Lân, Ngô Tất Tố đã phản ánh chân thực số phận cùng cực của người nông dân dưới ách thống trị tàn bạo của thực dân phong kiến. Đồng thời, tác phẩm ngời sáng chủ nghĩa nhân đạo sâu sắc khi phát hiện và ngợi ca phẩm giá cao đẹp, lòng tự trọng và khát vọng sống thiện lương dù bị đẩy vào bờ vực bần cùng hóa."
    },
    {
        "id": "doc_eng_01",
        "domain": "english",
        "title": "The Environmental Impacts of Renewable Energy Transitions",
        "content": "While the transition to renewable energy sources such as solar photovoltaics and wind turbines significantly reduces greenhouse gas emissions, it brings new ecological considerations. The fabrication of solar cells requires rare earth elements and toxic chemicals, whereas large-scale wind farms may disrupt migratory bird pathways and alter local acoustics. Consequently, sustainable energy policies must incorporate circular economy principles, rigorous recycling programs, and strategic environmental impact assessments."
    }
]

def tokenize(text: str) -> List[str]:
    """Tách từ đơn giản cho BM25 / Cosine similarity"""
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return words

def compute_tf_idf_similarity(query_tokens: List[str], doc_tokens: List[str]) -> float:
    """Tính cosine similarity thô dựa trên tần suất từ"""
    query_set = set(query_tokens)
    if not query_set or not doc_tokens:
        return 0.0
    
    doc_count = {}
    for w in doc_tokens:
        doc_count[w] = doc_count.get(w, 0) + 1
        
    dot_product = sum(doc_count.get(w, 0) for w in query_set)
    doc_magnitude = math.sqrt(sum(c * c for c in doc_count.values()))
    query_magnitude = math.sqrt(len(query_set))
    
    if doc_magnitude == 0 or query_magnitude == 0:
        return 0.0
    return dot_product / (query_magnitude * doc_magnitude)

class HyDERetriever:
    """
    HyDE Retriever: Hypothetical Document Embeddings
    1. Tiếp nhận chủ đề/câu hỏi người dùng.
    2. Sinh một đoạn văn bản giả định (Hypothetical Passage) giàu chi tiết học thuật.
    3. Dùng đoạn giả định để đối sánh và truy xuất tài liệu tương đồng nhất từ Knowledge Base.
    """
    def __init__(self, docs: List[Dict[str, Any]] = None):
        self.docs = docs or CURATED_KNOWLEDGE_DOCS

    def generate_hypothetical_document(self, topic: str, domain: str = "") -> str:
        """
        Sinh đoạn văn bản học thuật giả định (Hypothetical Document).
        Nếu có OpenAI API key, gọi LLM. Nếu không, sinh bằng mẫu kiến thức cấu trúc.
        """
        if OPENAI_API_KEY:
            try:
                from openai import OpenAI
                client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
                prompt = f"""Hãy viết một đoạn văn bản khoa học, ngắn gọn (khoảng 80-120 từ) trích từ sách giáo khoa chuyên sâu hoặc tài liệu khảo thí ĐGNL về chủ đề sau:
Chủ đề: {topic}
Lĩnh vực: {domain}
Đoạn văn cần chứa các thuật ngữ chuyên môn chính xác, dữ liệu định lượng, hiện tượng và bản chất khoa học để làm ngữ liệu truy xuất."""
                res = client.chat.completions.create(
                    model=OPENAI_MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.5,
                    max_tokens=250
                )
                return res.choices[0].message.content.strip()
            except Exception as e:
                print(f"HyDE LLM generation fallback: {e}")

        # Heuristic hypothetical passage generation
        return f"Tài liệu nghiên cứu chuyên đề {topic} thuộc lĩnh vực {domain}. Nội dung tập trung phân tích bản chất cơ chế, các định luật và nguyên lý chi phối, đánh giá tác động định lượng và giải pháp thực tiễn ứng dụng trong giải quyết vấn đề khoa học chuẩn ĐGNL."

    def retrieve(self, topic: str, domain: str = "", top_k: int = 2) -> Tuple[str, List[Dict[str, Any]]]:
        """
        Thực hiện HyDE Retrieval:
        1. Sinh Hypothetical Doc.
        2. Query Vector/Similarity matching với Knowledge Base.
        3. Trả về hypothetical_doc và danh sách top_k tài liệu liên quan nhất.
        """
        hypothetical_doc = self.generate_hypothetical_document(topic, domain)
        search_query = f"{topic} {domain} {hypothetical_doc}"
        query_tokens = tokenize(search_query)

        scored_docs = []
        for doc in self.docs:
            doc_tokens = tokenize(f"{doc['title']} {doc['content']} {doc.get('domain', '')}")
            score = compute_tf_idf_similarity(query_tokens, doc_tokens)
            
            # Boost nếu trùng domain
            if domain and doc.get("domain") == domain:
                score += 0.25

            scored_docs.append((score, doc))

        scored_docs.sort(key=lambda x: x[0], reverse=True)
        top_docs = [item[1] for item in scored_docs[:top_k]]
        return hypothetical_doc, top_docs
