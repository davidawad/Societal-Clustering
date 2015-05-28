
import indicoio
indicoio.config.api_key = "13aaf3fb916e24d4d31bc4bf3e79cd6f"

tag_dict = indicoio.text_tags("Iran Agrees to Nuclear Limits, But Key Issues Are Unresolved")

print(sorted(tag_dict.keys(), key=lambda x: tag_dict[x], reverse=True)[:5])
