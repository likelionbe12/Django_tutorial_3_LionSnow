from typing import Any
from django.db import models

# Create your models here.
class ImagePost(models.Model):
    # title, --image--, desription, create_at, update_at, author
    title=models.CharField(max_length=100, verbose_name="제목")
    image = models.ImageField(upload_to='lion_images/', verbose_name="이미지") ##!!
    description=models.TextField(verbose_name='설명')
    create_at=models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    update_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='작성자')

    class Meta:        
        ordering=['-create_at']
        verbose_name = '이미지 게시글'
        verbose_name_plural = '이미지 게시글들'

    def __str__(self) -> str:
        return self.title
    
    # 이미지 게시글 삭제하면, 이미지 파일도 삭제하기
    def delete(self, *args, **kwargs):
        # 이미지 파일도 함께 삭제
        if self.image:
            self.image.delete()
            super().delete( *args, **kwargs)

    # 관리자 페이지에 접속해서 이미지를 올리고 지워보겠습니다
    # image가 어떻게 저장되고 관리되는지 살펴보기
    # delete도 잘 되는지 확인하기
    # 2:25분까지
