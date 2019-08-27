import Vapor

public struct Empty : Codable {
public init() {}
}

extension Empty : Content {}
