init:
	mkdir working_folder
import:
	gpg --import cw_recruitment.gpg
encrypt:
	@mkdir -p publish_folder
	@echo "Files to be included in the deliverable:"
	@find working_folder/ -type f
	@tar -c working_folder/ | gpg --encrypt --batch --yes --trust-model always -r jobs@coverwallet.com --output publish_folder/exercise.gpg
	@echo "Deliverable created in: ./publish_folder/exercise.gpg"

# Only available for CoverWallet recruiters
decrypt:
	gpg --decrypt publish_folder/exercise.gpg | tar x
clean:
	rm -rf publish_folder
