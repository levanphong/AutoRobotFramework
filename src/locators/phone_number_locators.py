# PHONE AI
ICON_ADD_AI_PHONE = "//i[@class='icon-plus']"
INPUT_AREA_CODE = "//form[@class='row bv-form']//input[@id='area-code']"
BUTTON_CONTINUE_MODAL_PHONE_AI = "//div[@class='modal-body clearfix']//button[@id='select-package']"
US_INTERNATIONAL_OPTION = "//div[@class='modal-body clearfix']//strong[contains(text(),'US & International')]"
ICON_SMS_ONLY_AI_PHONE = "//div[@class='modal-body clearfix']//strong[contains(text(),'US & International')]/preceding-sibling::div/i[@class='package-icon']"
BUTTON_GENERATE = "//form[@class='row bv-form']//button[@class='btn btn-primary next-btn'][contains(text(),'Generate number')]"
JOB_SEARCH_TOGGLE_PHONE_AI = "//label[contains(@for,'job_search_on') and text()='Job Search']"
KNOWLEDEGE_BASE_PHONE_AI = "//label[contains(@for,'knowledge_base')]"
ADD_ATTRIBUTE_PHONE_AI = "//*[contains(@id,'job-search-attributes-wrapper')]/parent::div//button"
CURRENTLY_UNUSED = "//div[contains(text(),'(currently unused)')]"
INPUT_ATTRIBUTE_VALUE = "(//*[contains(@name,'attribute_values')])[{}]"
PHONE_AI_PHONE_NUMBER_OPTION_LAST = "(//div[contains(@class, 'card-content')]//div[contains(@id, 'phone-numbers')]//span[contains(@class, 'phone')])[last()]"
PHONE_AI_CLICK_PHONE_NUMBER_BY_CONVERSATION = "//div[contains(@class, 'card-content')]//div[contains(@id, 'phone-numbers')]//div[contains(text(), '{}')]//following-sibling::i"
PHONE_AI_JOB_SEARCH_TOGGLE = "//div[contains(@id, 'form_ai_phone_container')]//label[contains(@for, 'job_search_on')]"
PHONE_AI_ALL_JOB_FEED_DROPDOWN = "//input[contains(@value, 'Default job feed')]"
PHONE_AI_PHONE_NUMBER_TYPE = "//strong[contains(@class, '_lead_name') and contains(text(), '{}')]"
PHONE_AI_CANCEL_JOB_FEED_BUTTON = "//*[contains(@class, 'popover-content')]//button[contains(@class, 'cancel-btn')]"
PHONE_AI_APPLY_JOB_FEED_BUTTON = "//*[contains(@class, 'popover-content')]//button[contains(@class, 'btn-apply')]"
PHONE_AI_CAPTURE_CONVERSATION_DROPDOWN = "//*[contains(@id, 'id_start_interaction_type')]"
PHONE_AI_DELETE_BUTTON = "//*[contains(@class, 'btn-remove')]"
PHONE_AI_CONFIRM_DELETE_BUTTON = "//*[contains(@class, 'ok-btn') and contains(text(), 'Yes')]"
PHONE_AI_FORM_JOB_SEARCH_TOGGLE = "//div[contains(@id, 'form_ai_phone_container')]//label[contains(@for, 'job_search_on')]"
PHONE_AI_FORM_ALL_JOB_FEED_DROPDOWN = "//input[contains(@value, 'Default job feed')]"
PHONE_AI_FORM_SELECT_ALL_JOB_FEED_CHECKBOX = "//div[contains(@class, 'fade bottom in')]//label[contains(normalize-space(), 'Select All Job Feeds')]"
PHONE_AI_FORM_JOB_FEED_OPTION = "//*[@id='mCSB_3_container']//label[normalize-space()='{}']"
PHONE_AI_FORM_CANCEL_BUTTON = "//button[contains(@class, 'btn-default cancel-btn')]"

# SHORTCODE
SHORT_CODE_MODAL = "(//div[contains(@class,'box')]//strong[contains(text(),'US Shortcode')])[2]"
BUTTON_CONTINUE_MODAL_SHORT_CODE = "//div[contains(@class,'modal-dialog modal-xs')]//button[contains(text(),'Continue')]"
INPUT_SHORT_CODE_KEYWORD = "(//*[contains(@id,'step_create_shortcode')]//*[contains(@id,'id_shortcode_keyword')])[2]"
BUTTON_GENERATE_SHORTCODE = "//form[contains(@class, 'bv-form')]//button[contains(text(), 'Create Keyword')]"
JOB_SEARCH_TOGGLE_SHORTCODE = "//label[contains(@for,'loc_shortcode_job_search_on')]"
KNOWLEDEGE_BASE_SHORTCODE = "//label[contains(@for,'knowledge_base_loc_shortcode')]"
BUTTON_DELETE_SHORTCODE = "//button[contains(@class,'btn btn-default btn-remove')]"
ADD_ATTRIBUTE_SHORTCODE = "//div[contains(@id,'job-search-attributes-wrapper')]//button"
