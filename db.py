from pydantic import BaseModel, ConfigDict, Field


class Review(BaseModel):
    subject: str
    text: str
    mark: int = Field(le=10, ge=0)
    model_config = ConfigDict(extra='forbid')

REVIEWS=[]
# Получаем все отзывы, которые есть 
async def get_saved_reviews():
    return REVIEWS


# Сохраняем отзыв
async def save_review(review: Review):
    REVIEWS.append(review)


#  Очищение списка
async def delete_all_reviews():
    REVIEWS.clear()