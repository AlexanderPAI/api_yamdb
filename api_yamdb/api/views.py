from django.shortcuts import render

# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    """Представление модели комменатриев."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def get_queryset(self):
        return super().get_queryset().filter(
            post_id=self.kwargs.get('post_id')
        )

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

