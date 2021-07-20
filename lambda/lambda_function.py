# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, you can say what kind of food info do you offer"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class FoodInfoIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FoodInfoIntent")(handler_input)
        
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        question = slots["question"].value
        if question == "what kind of food info do you offer":
            speak_output = "We offer info about about common food misconceptions, dangerous food, foods that you should avoid, and balanced meals."
        elif question == "what are my options":
            speak_output = "You can ask me about deficiencies, cacao, canned tuna, supplements, m. s. g., dangerous foods, balanced meals, heavy metals, gluten, and organic foods.w"
        
        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
            )
class FoodRequestIntentHandler(AbstractRequestHandler):
        
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FoodRequestIntent")(handler_input)
        
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        question = slots["question"].value
        
        if question == "iron deficiency":
            speak_output = "As the name implies, iron deficiency anemia is due to insufficient iron. Without enough iron, your body can't produce enough of a substance in red blood cells that enables them to carry oxygen. You can prevent this by eating foods high in iron like spinach or supplements"
        elif question == "common deficiencies":
            speak_output = "Common deficiencies include vitamin a, magnesium, omega three, vitamin b twelve, vitamin d, iodine, and iron."
        elif question == "iodine deficiency":
            speak_output = "Iodine is an element that is needed for the production of thyroid hormone. The body does not make iodine, so it is an essential part of your diet. A deficiency can result in irregular thyroid activity. You can eat fish and dairy to raise iodine levels"
        elif question == "vitamin d deficiency":
            speak_output = "Although there is no clear symptoms for vitamin d deficiency, it may result in lowered mood and more irritability. You can get vitamin d by spending more time in the sun."
        elif question == "vitamin b twelve deficiency":
            speak_output = "Vitamin b twelve deficiency may lead to anemia, weakness, or neverous system damage. Meats contain high amounts of vitamin b twelve"
        elif question == "omega three deficiency":
            speak_output = "Omega three deficiency will result in brittle hair, nails, skin, and fatigue. To get more omega three, eat fish or take supplements."
        elif question == "magnesium deficiency":
            speak_output = "magnesium deficiency can result in muscle twitches, cramps, and mental health disorders. Nuts and avocado contain high amounts of magnesium."
        elif question == "vitamin a deficiency":
            speak_output = "vitamin a deficiency can result in dry skin and dry eyes. Liver and fish contain high amounts of vitamin a"
        elif question == "cacao":
            speak_output = "Cacao is commonly found in chocolate. The way cacao is harvested can be quite dangerous because the shell of cacao contains high amounts of heavy metals like cadmium and mercury. When eating dark chocolate, be careful when eating more than the recommended amount"
        elif question == "canned tuna":
            speak_output = "canned tuna contains high amounts of heavy metals and should be eaten in moderation. Though tuna can be quite healthy"
        elif question == "balanced meal":
            speak_output = "a balanced meal contains a quarter carbohydrates, a quarter proteins, and half vegetables."
        elif question == "supplements":
            speak_output = "things that can be taken in a day if you have a deficiency or lack of nutrition. Certain supplements like magnesium and omega three, depending on the company, can contain high amounts of arsenic and other heavy metals. "
        elif question == "monosodium glutamate":
            speak_output = "m s g is commonly found in cheese and processed foods. m s g has no adverse effects on human and it is okay to be consumed."
        elif question == "dangerous":
            speak_output = "cherry pits, fugu, cashews, raw eggs, fermented cheese, and potatoes that are stored for too long."
        elif question == "heavy metals": 
            speak_output = "Fish, cacao, and rice. heavy metals include arsenic, lead, cadmium, mercury, copper, and more. Symptoms of heavy metal poisioning include nausea, vomiting, diarrhea, shortness of breath, tingling in hands and feet, and chills."
        elif question == "gluten bad for you":
            speak_output = "If you don't have celiac disease or any other side effects from eating gluten, there is no need to be worried about consuming gluten. Gluten is common in foods such as bread, pasta, and cereal"
        elif question == "eating foods before bed bad for you":
            speak_output = "Unless you eat a higher amount of calories than you normally do, there is no harm in eating before bed. There isn't concrete evidence in proving that it is unhealthy, especially for a normal diet."
        elif question == "organic foods more nutritious":
            speak_output = "There is no evidence proving that organic foods are healthier than inorganic foods. While genetically modified foods may contain pesticides, organic foods may contain bacteria."
        elif question == "eating before bed bad for you":
            speak_output = "The short answer is no, eating before bed isn't bad for you as long as you hit your macros and aren't eating in a caolric surplus. Although eating before bed may intefere with your sleep"
        else:
            speak_output = "I am not sure what you mean"
        
        return (
            handler_input.response_builder.speak(speak_output).ask(speak_output).response
            )

class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(FoodInfoIntentHandler())
sb.add_request_handler(FoodRequestIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()