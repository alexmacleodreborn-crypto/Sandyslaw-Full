export const GATES = {
  PROTO_COGNITION: {
    memoryWrite: false,
    awareness: false,
    identity: false,
    actionGating: true,
  },
  MAX_STAGE: 2,
};

export function assertStage(stage: number) {
  if (stage > GATES.MAX_STAGE) {
    throw new Error("Stage gate violated: STG-3 not enabled");
  }
}
