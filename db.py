from pydantic import BaseModel, ConfigDict, Field


class Review(BaseModel):
    subject: str
    text: str
    mark: int = Field(le=10, ge=0)
    model_config = ConfigDict(extra='forbid')
    id: int | None = None

REVIEWS=[]
# Получаем все отзывы, которые есть 
async def get_saved_reviews():
    return REVIEWS


# Сохраняем отзыв
async def save_review(review: Review):
    if not review.id:
        review.id = len(REVIEWS) + 1
    REVIEWS.append(review)


#  Очищение списка
async def delete_all_reviews():
    REVIEWS.clear()