from django.db.models import QuerySet


def all_objects(model, select_related: str = None, prefetch_related: str = None) -> QuerySet:
    """Get all objects for a given model.

    Args:
    - model: The model for which to retrieve objects
    - select_related: Related fields to select in the query
    - prefetch_related: Related fields to prefetch in the query

    """
    all_objects = model.objects.all()
    if select_related:
        all_objects = all_objects.select_related(select_related)
    if prefetch_related:
        all_objects = all_objects.prefetch_related(prefetch_related)
    return all_objects


def get_object(model, **kwargs) -> QuerySet:
    """
    Get a single object of the given model based on provided criteria

    Args:
    - model: The model for which to get filtered objects
    - **kwargs: Filtering criteria for retrieving objects

    """
    return model.objects.get(**kwargs)


def get_filter_objects(model, **kwargs) -> QuerySet:
    """
    Get filtered objects for the given model based on provided criteria.

     Args:
    - model: The model for which to retrieve filtered objects
    - **kwargs: Filtering criteria for retrieving objects


    """
    return model.objects.filter(**kwargs)
