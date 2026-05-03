import markdown
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.html import escape

from .models import ChatMessage
from .services import get_ai_response


@login_required
def chatbot(request):
    chats = ChatMessage.objects.filter(user=request.user).order_by("created_at")

    if request.method == "POST":
        message = request.POST.get("message", "").strip()

        if not message:
            messages.error(request, "Please type a message before sending.")
            return redirect("chatbot")

        try:
            response = get_ai_response(message)
        except Exception:
            response = (
                "Sorry, the AI service is unavailable right now. "
                "Please try again soon."
            )

        formatted_response = markdown.markdown(
            escape(response),
            extensions=["extra", "sane_lists"],
            output_format="html",
        )

        ChatMessage.objects.create(
            user=request.user,
            message=message,
            response=formatted_response,
        )

        return redirect("chatbot")

    return render(request, "chatbot/chat.html", {"chats": chats})


@login_required
def clear_chat(request):
    if request.method == "POST":
        ChatMessage.objects.filter(user=request.user).delete()
        messages.success(request, "Chat history cleared.")
    return redirect("chatbot")
