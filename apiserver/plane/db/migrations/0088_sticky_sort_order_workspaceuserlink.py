# Generated by Django 4.2.15 on 2024-12-24 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0087_remove_issueversion_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name="sticky",
            name="sort_order",
            field=models.FloatField(default=65535),
        ),
        migrations.CreateModel(
            name="WorkspaceUserLink",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last Modified At"
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Deleted At"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("url", models.TextField()),
                ("metadata", models.JSONField(default=dict)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created By",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner_workspace_user_link",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_%(class)s",
                        to="db.project",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_updated_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Last Modified By",
                    ),
                ),
                (
                    "workspace",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workspace_%(class)s",
                        to="db.workspace",
                    ),
                ),
            ],
            options={
                "verbose_name": "Workspace User Link",
                "verbose_name_plural": "Workspace User Links",
                "db_table": "workspace_user_links",
                "ordering": ("-created_at",),
            },
        ),
        migrations.AlterField(
            model_name="pagelog",
            name="entity_name",
            field=models.CharField(max_length=30, verbose_name="Transaction Type"),
        ),
        migrations.AlterUniqueTogether(
            name="webhook",
            unique_together={("workspace", "url", "deleted_at")},
        ),
        migrations.AddConstraint(
            model_name="webhook",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted_at__isnull", True)),
                fields=("workspace", "url"),
                name="webhook_url_unique_url_when_deleted_at_null",
            ),
        ),
    ]
