class OwnLinkQuerysetMixin:
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class OwnTagQuerysetMixin:
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(links_taggedlink_items__content_object__user=self.request.user)
            .distinct()
        )
