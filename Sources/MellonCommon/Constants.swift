
import Foundation

public enum Environment: String {
    case mongoURL = "MONGODB_URL"
    case slackOAuthAccessToken = "SLACK_OAUTH_ACCESS_TOKEN"
    case slackBotOAuthAccessToken = "SLACK_BOT_OAUTH_ACCESS_TOKEN"
    case slackClientId = "SLACK_CLIENT_ID"
    case slackClientSecret = "SLACK_CLIENT_SECRET"
    case slackVerificationToken = "SLACK_VERIFICATION_TOKEN"
    case slackSigningSecret = "SLACK_SIGNING_SECRET"
    case sentryDSN = "SENTRY_DSN"
}

public struct Constants {
public static let CURRENT_API_VERSION = "1"
}
