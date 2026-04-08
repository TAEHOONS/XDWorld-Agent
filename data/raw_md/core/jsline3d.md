---
description: 지도 내 선을 생성 관리하기 위한 API 입니다.
---

# JSAABBox3D

> Module.JSLine3D() API를 생성합니다.

```javascript
let start = new Module.JSVector3D(129.14, 35.18, 100.0);
let end = new Module.JSVector3D(129.18, 35.189, 200.0);
let lineDefault = new Module.JSLine3D();
let lineWithStartEnd = new Module.JSLine3D(start, end);
```

## properties

| Name  | Type                                | Description          |
| :---- | :---------------------------------- | :------------------- |
| start | [JSVector3D](../core/jsvector3d.md) | 선의 시작 위치 좌표. |
| end   | [JSVector3D](../core/jsvector3d.md) | 선의 조욜 위치 좌표. |
